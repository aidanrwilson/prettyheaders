from .styles import CALVIN_S_FONT, S_SEGS, D_SEGS, A_SEGS
import numpy as np


def style_dict(style):
    if style == 'single':
        return S_SEGS
    if style == 'double':
        return D_SEGS
    if style == 'arc':
        return A_SEGS
    raise ValueError('Specified style, %s, currently not supported.' % style)

def top_bar(plen, style='double'):
    S = style_dict(style)
    return S['down-right'] + (plen + 2)*S['horizontal'] + S['down-left']

def bottom_bar(plen, style='double'):
    S = style_dict(style)
    return S['up-right'] + (plen + 2)*S['horizontal'] + S['up-left']

def _npencode_char(c):
    return np.array([[ord(_c) for _c in row] for row in CALVIN_S_FONT[c]], dtype=np.uint32)

def _npencode_line(s):
    return np.hstack([_npencode_char(c) for c in s])

def pvstack(arrs, pad=True):
    if not pad:
        return np.vstack(arrs)
    arr = np.zeros((3 * len(arrs), np.max([_arr.shape[1] for _arr in arrs])), dtype=np.uint32)
    for i, _arr in enumerate(arrs):
        arr[3*i : 3*(i+1), : _arr.shape[1]] = _arr
    return arr
np.pvstack = pvstack

def npencode(s):
    if not isinstance(s, str):
        raise ValueError('npencode got parameter s not of type str (single character or string)!')
    return pvstack([_npencode_line(r_i) for r_i in s.split('\n')])

def npdecode(s_n):
    if len(s_n.shape) == 2:
        s_n = s_n[None, :, :]
    return '\n\n'.join(['\n'.join([''.join([chr(s_n[i][j][k]) for k in range(s_n.shape[2])])
                                                              for j in range(s_n.shape[1])])
                                                              for i in range(s_n.shape[0])])

def pheader(s, box=True, style='double'):
    pstr = npdecode(npencode(s))
    if not box:
        return pstr
    S = style_dict(style)
    L_SIDE = S['vertical'] + ' '
    R_SIDE = ' ' + S['vertical']
    pstr = pstr.split('\n')
    plen = np.max([len(pstr_i.rstrip()) for pstr_i in pstr])
    pstr = [pstr_i[:plen] for pstr_i in pstr]
    return ( top_bar(plen, style) + '\n' + L_SIDE
             + (R_SIDE + '\n' + L_SIDE).join(pstr)
             + R_SIDE + '\n' + bottom_bar(plen, style) )
