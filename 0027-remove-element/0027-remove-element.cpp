class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int right = std::size(nums);
        int left = 0;

        while ( right > left) {
            if(nums[left] == val) {
                nums[left] = nums[right - 1];
                right--;
            }
            else{
                left++;
            }
        }
        return right;
    }
};