double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    // Ensure nums1 is the smaller array
    if (nums1.size() > nums2.size())
        return findMedianSortedArrays(nums2, nums1);

    int m = nums1.size(), n = nums2.size();
    int low = 0, high = m;

    while (low <= high) {
        int partition1 = (low + high) / 2;
        int partition2 = (m + n + 1) / 2 - partition1;

        // Handle edge cases with -INF and +INF
        int maxLeft1 = (partition1 == 0) ? INT_MIN : nums1[partition1 - 1];
        int minRight1 = (partition1 == m) ? INT_MAX : nums1[partition1];

        int maxLeft2 = (partition2 == 0) ? INT_MIN : nums2[partition2 - 1];
        int minRight2 = (partition2 == n) ? INT_MAX : nums2[partition2];

        // Check if we found the correct partition
        if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
            // Found the median!
            if ((m + n) % 2 == 0) {
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0;
            } else {
                return max(maxLeft1, maxLeft2);
            }
        }
        // Adjust binary search
        else if (maxLeft1 > minRight2) {
            high = partition1 - 1;  // Move left in nums1
        } else {
            low = partition1 + 1;   // Move right in nums1
        }
    }
    return 0.0;
}

int main(){
    vector<int>& nums1 = [1,2,3,4]
    vector<int>& nums2 = [1,2,3,4]
    res = findMedianSortedArrays(nums1, nums2)
    return res
}