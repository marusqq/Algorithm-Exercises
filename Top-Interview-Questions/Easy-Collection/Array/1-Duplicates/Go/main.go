package main

import "fmt"

func main() {
	var nums = []int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}
	fmt.Printf("Answer: %d \n", removeDuplicates(nums))
}

func removeDuplicates(nums []int) int {
	var current_value int = -99
	var next_value int = -99

	for i := 0; i < len(nums); i++ {
		current_value = next_value
		next_value = nums[i]
		if current_value == next_value {
			nums = append(nums[:i], nums[i+1:]...)
			i--
		}

	}
	fmt.Printf("%d\n", nums)
	return len(nums)
}
