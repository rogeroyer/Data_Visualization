def drawPillar():
    n_groups = 5
    means_men = (20, 35, 30, 35, 27)
    means_women = (25, 32, 34, 20, 25)

    # plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.3

    opacity = 0.4
    plt.bar(index, means_men, bar_width, alpha=opacity, color='b', label='Men')
    plt.bar(index + bar_width, means_women, bar_width, alpha=opacity, color='r', label='Women')

    plt.xlabel('Group')
    plt.ylabel('Scores')
    plt.title('Scores by group and gender')
    plt.xticks(index + bar_width / 2, ('A', 'B', 'C', 'D', 'E'))
    plt.ylim(0, 40)
    plt.legend()

    plt.tight_layout()
    plt.show()


drawPillar()
