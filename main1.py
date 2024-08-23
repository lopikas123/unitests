def count_vowels(s):
    vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouAEIOU'
    return sum(1 for char in s if char in vowels)