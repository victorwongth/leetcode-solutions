func twoSum(nums []int, target int) []int {
    hashmap := make(map[int]int)
    for i, v := range nums {
        diff := target - v 
        if value, ok := hashmap[diff]; ok {
            return []int{value, i}
        } else {
            hashmap[v] = i 
        }
    }
    return []int{}
}
