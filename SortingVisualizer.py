import SortingAlgorithms
import pygame
import time
import sys

algorithms = [SortingAlgorithms.SelectionSort(), SortingAlgorithms.InsertionSort(), SortingAlgorithms.MergeSort()]

pygame.init()
display = pygame.display.set_mode((1024,512))
display.fill((255,255,255))


def close_window():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def keep_open(algorithm, display, time):
    pygame.display.set_caption(f'Sorting using {algorithm.name}  Completed in: {time} seconds')
    while True:
        close_window()
        pygame.display.update()

def update_window(algorithm , index1 = None, index2 = None, display =display):
    display.fill((255,255,255))
    pygame.display.set_caption(f'Sorting using {algorithm.name}  Time: {time.time()-algorithm.start_time}')
    dim = int(1024/len(algorithm.array_to_sort))
    for i in range(len(algorithm.array_to_sort)):
        stick_color = (0,0,255)
        if index1 == algorithm.array_to_sort[i]:
            stick_color = (0,255,0)
        elif index2 == algorithm.array_to_sort[i]:
            stick_color = (255,0,0)
        
        pygame.draw.rect(display, stick_color, (i*dim, 512, dim, -algorithm.array_to_sort[i]),1)
    close_window()
    pygame.display.update()



def main():
    print("""Please input the number corresponding to the sorting algorithm you wish to test:
1-Selection Sort
2-Insertion Sort
3-Merge Sort
    \n\n\n""")
    flag = True
    while flag == True:
        selected_algorithm = (input("Enter the corresponding number here: "))
        if selected_algorithm in ("1","2","3"):
            break
        else:
            print("This number doesn't match with any algorithm. Please enter a corresponding number: ")

    selected_algorithm = int(selected_algorithm)
    algo = algorithms[selected_algorithm-1]
    time = algo.run()[1]
    keep_open(algo, display, time)

if __name__ == "__main__":
    main()


