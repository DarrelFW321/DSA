// Last updated: 2/11/2026, 11:08:46 AM
object Solution {
    def isPalindrome(x: Int): Boolean = {
        if (x < 0 || (x % 10 == 0 && x != 0)) return false

        var num = x
        var reversed = 0

        while (num > reversed) {
        reversed = reversed * 10 + num % 10
        num /= 10
        }

        num == reversed || num == reversed / 10
    }
}