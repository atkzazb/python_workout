def remove_authors(s, L):
    out = s
    for name in L:
        out = out.replace(name, '_' * len(name))
        
    return out

print(remove_authors('SGKLFSGKL SFKJFSH SGLSH SHKS Fisher Thomas', ['Fisher', 'Thomas']))