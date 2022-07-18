package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	f, err := os.Open("day11.txt")
	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	scanner := bufio.NewScanner(f)

	grid := [][]int{}

	for scanner.Scan() {
		// do something with a line
		a := strings.Split(scanner.Text(), "")

		var t2 = []int{}

		for _, i := range a {
			j, err := strconv.Atoi(i)
			if err != nil {
				panic(err)
			}
			t2 = append(t2, j)
		}

		grid = append(grid, t2)

	}

	// fmt.Println(grid)
	// fmt.Println(incrementAll(grid))

	for i := 0; i < 1000; i++ {
		flashCount := 0
		grid = incrementAll(grid)
		runCount := -1

		for {
			runCount += 1
			// fmt.Println("runCount: ", runCount)
			if !checkNines(grid) {
				break
			}

			for udIndex, udValue := range grid {
				for lrIndex, lrValue := range udValue {
					// fmt.Println(lrValue)
					if lrValue > 9 {
						// then it flashes
						flashCount += 1
						isBottomRow := udIndex == len(grid)-1 // true if it is the bottom row
						isTopRow := udIndex == 0
						isLeftColumn := lrIndex == 0
						isRightColumn := lrIndex == len(udValue)-1

						grid[udIndex][lrIndex] = -100

						// fmt.Println("udIndex: ", udIndex, "lrIndex: ", lrIndex, "flashCount: ", flashCount)

						if !isBottomRow {
							grid[udIndex+1][lrIndex] = grid[udIndex+1][lrIndex] + 1

							if !isLeftColumn {
								grid[udIndex+1][lrIndex-1] = grid[udIndex+1][lrIndex-1] + 1
							}
							if !isRightColumn {
								grid[udIndex+1][lrIndex+1] = grid[udIndex+1][lrIndex+1] + 1
							}
						}

						if !isTopRow {
							grid[udIndex-1][lrIndex] = grid[udIndex-1][lrIndex] + 1

							if !isLeftColumn {
								grid[udIndex-1][lrIndex-1] = grid[udIndex-1][lrIndex-1] + 1
							}

							if !isRightColumn {
								grid[udIndex-1][lrIndex+1] = grid[udIndex-1][lrIndex+1] + 1
							}
						}

						if !isLeftColumn {
							grid[udIndex][lrIndex-1] = grid[udIndex][lrIndex-1] + 1
						}

						if !isRightColumn {
							grid[udIndex][lrIndex+1] = grid[udIndex][lrIndex+1] + 1
						}

					}

				}
			}
		}

		if flashCount == 100 {
			fmt.Println("run number: ", i)
			break
		}

		grid = fixNegatives(grid)
		fmt.Println(grid)

		if err := scanner.Err(); err != nil {
			log.Fatal(err)
		}
	}

}

func incrementAll(grid [][]int) [][]int {
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			grid[i][j] = grid[i][j] + 1
		}
	}

	return grid
}

func checkNines(grid [][]int) bool {
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			if grid[i][j] > 9 {
				return true
			}
		}
	}

	return false
}

func fixNegatives(grid [][]int) [][]int {
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			if grid[i][j] <= 0 {
				grid[i][j] = 0
			}
		}
	}

	return grid
}
