// Last updated: 2/11/2026, 11:08:54 AM
import scala.collection.mutable.HashMap
import scala.util.boundary, boundary.break

object Solution {
    def twoSum(nums: Array[Int], target: Int): Array[Int] = {
        val seen = HashMap[Int, Int]()

        boundary {
            for (i <- nums.indices) {
                val complement = target - nums(i)
                if (seen.contains(complement)) {
                    break(Array(seen(complement), i))
                }
                seen(nums(i)) = i
            }
            Array()
        }
    }
}