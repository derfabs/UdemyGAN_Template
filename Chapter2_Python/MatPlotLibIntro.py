import matplotlib.pyplot as plt

grades_jan = [56, 64, 78, 100]
grades_ben = [86, 94, 98, 90]

# Noten als Plot
plt.plot(range(len(grades_jan)), grades_jan)
plt.plot(range(len(grades_ben)), grades_ben)
plt.legend(["Jan", "Ben"])
plt.xlabel("Course")
plt.ylabel("Grade in %")
plt.title("Notenübersicht")
plt.show()

# Noten als Einzelpunkte
plt.scatter(range(len(grades_jan)), grades_jan)
plt.scatter(range(len(grades_ben)), grades_ben)
plt.legend(["Jan", "Ben"])
plt.xlabel("Course")
plt.ylabel("Grade in %")
plt.title("Notenübersicht")
plt.show()
