def k(s):
    b = 0
    for c in s:
        if b:
            b = 0
            print(c, end='')
        elif c == '_': b = 1
        elif 1: print({'f':'for','i':'in','j':'if','d':'def','e':'elif','p':'print'}.get(c, c), end='')
    print("'''" + s + "''')")

k('''d k(s):
    b = 0
    f c i s:
        j b:
            b = 0
            p(c, _e_n_d='')
        e c == '__': b = 1
        e 1: p({'_f':'_for','_i':'_i_n','_j':'_i_f','_d':'_d_e_f','_e':'_el_i_f','_p':'_prit'}.g_et(c, c), _e_n_d='')
    p("'_''" + s + "'_'')")

k(''')
