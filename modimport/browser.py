import webbrowser
# # docs 21.1
# webbrowser.open("https://www.python.org/")
#
# help(webbrowser)
# ===========================
# for i in range(10):
#     print(1, 2, 3, 4, 5, 6, 7, 8, 9)
#     # there is a space
# ===========================

# for i in range(10):
#     print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep=";", end=" ")
#     print()

# =======================
# import webbrowser
#
# webbrowser.open("https://www.python.org/", new="2")
# if possible in the documentation means that if the browser is
# allowing it , it will open in a new window

# ========================
# this code didn't work
# chrome = webbrowser.get("google-chrome %s").open_new_tab("https://www.python.org/")
# chrome.open_new("https://www.python.org/")

# this code worked for safari for mac specific
safari = webbrowser.get(using='safari')
safari.open("https://www.python.org/")


