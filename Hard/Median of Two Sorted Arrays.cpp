#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        int m = nums2.size();
        // No need to sort since they are already sorted
        
        // Merge the vectors using the merge function
        vector<int> merged(n + m);
        merge(nums1.begin(), nums1.end(), nums2.begin(), nums2.end(), merged.begin());

        // Calculate median based on the total length of the merged array
        if ((n + m) % 2 != 0) {
            // Odd total length, return the middle element
            return (double)merged[(n + m) / 2];
        } else {
            // Even total length, return the average of the two middle elements
            return (double)(merged[(n + m - 1) / 2] + merged[(n + m) / 2]) / 2.0;
        }
    }
};
