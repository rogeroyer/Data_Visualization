def drawStar():
    plt.figure(figsize=(8, 4))
    x = np.random.random(100)
    y = np.random.random(100)
    plt.scatter(x, y, s=x * 1000, c='y', marker='*', alpha=0.5, lw=2, edgecolors='blue')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.show()


drawStar()
