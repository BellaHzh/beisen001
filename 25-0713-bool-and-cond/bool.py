score = int(input('Enter your score: '))

validated_and = score >= 0 and score <= 100
validated_or = not (score < 0 or score > 100)

print(f'validated with and: {validated_and}')
print(f'validated with or: {validated_or}')
