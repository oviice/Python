x = 101


# Global variable in function
def ovi():
    global x
    x = 69

    print(x)
    # modifying a global variable
    x = 'Welcome To Javatpoint'
    print(x)


ovi()
print(x)
