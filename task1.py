# Напишите код, который спрашивает имя и фамилию пользователя. Сделайте так чтоб на
# экран вышла первая буква имена, точка и фамилия полностью с приветствием.
firstname = input('пожалуйста, введите ваше имя: ')
lastname = input('пожалуйста, введите вашу фамилию: ')
print(firstname[0].title() + '.' + lastname.title() + ', hello!') 