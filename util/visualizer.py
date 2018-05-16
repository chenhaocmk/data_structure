

def print_tree(root, level_func, val_func=None):

    def _dfs(node, n):
        print(n * '    ' + ' ' +
              str(val_func(node) if val_func else node))
        for child in level_func(node):
            _dfs(child, n+1)
    _dfs(root, 0)

