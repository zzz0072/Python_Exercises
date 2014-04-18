#/usr/bin/env python
g_var = "global"
def show_mod_var():
    try:
        print(g_var)
    except UnboundLocalError:
        print("You can not reference a global value inner function");
        pass
    # ref: https://docs.python.org/2/tutorial/classes.html#python-scopes-and-namespaces
    # Anywrite to this varalbe will cause a UnboundLocalError!!!!!
    # You can un-comment line 11 to test
    # g_var = 100
    print(g_var)

print(g_var)
show_mod_var()
g_var = "modified"
print(g_var)

if True:
    # if block can read global
    print(g_var)
    g_var = "modified 2"
    print(g_var)
