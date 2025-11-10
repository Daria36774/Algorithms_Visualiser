import matplotlib.pyplot as plt
import matplotlib.animation as animation
from algorithms.bubble_sort import bubble_sort
import random


def visualize_sort():
    arr = [random.randint(1, 100) for _ in range(30)]
    generator = bubble_sort(arr)
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")
    ax.set_title("Bubble Sort Visualisation")
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, 110)
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")


    def update(frame, rects):
        for rect, val in zip(rects, frame):
            rect.set_height(val)
        return rects

    anim = animation.FuncAnimation(
        fig, func=update,
        fargs=(bar_rects,),
        frames=generator,
        interval=50,
        repeat=False
    )

    plt.show()

if __name__ == "__main__":
    visualize_sort()