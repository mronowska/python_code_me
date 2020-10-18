men_name = input("Male name: ")
feature_positive = input("Positive feature of this man: ")
feature_negative = input("Negative feature of this man: ")
day_of_the_week = input("Day of the week: ")
place = input("Place: ")
animal = input("Animal: ")

print(
    f"There was a man called {men_name}. In one hand he was {feature_positive}, but on the other hand also a little {feature_negative}.\nOne day, I think it was {day_of_the_week}, {feature_negative} lost him. When he was walking on the {place}, he met {animal}, which ate people for being {feature_negative}. That's how he died.")

print("\n\n")

print(
    f"There was a man called {men_name}. In one hand he was {feature_positive}, but on the other hand also a little {feature_negative}.\nOne day, I think it was {day_of_the_week}, {feature_negative} lost him. When he was walking on the {place}, he met {animal}, which ate people for being {feature_negative}. That's how he died."[::-1])