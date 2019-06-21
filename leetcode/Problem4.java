public class Problem4 {
    public static void main(String[] args) {
        int[] nums1 = {1, 2};
        int[] nums2 = {3, 4};
        median(nums1, nums2);
    }

    static float median(int[] nums1, int[] nums2) {
        int total = nums1.length+nums2.length;
        int[] nums = new int[total];

        int i = 0;
        int j = 0;
        int k = 0;
        while (i + j + 2 < total) {
            if (nums1[i] < nums2[j]) {
                nums[k] = nums1[i];
                i++;
            } else {
                nums[k] = nums2[j];
                j++;
            }
            k++;
        }

        for(i = 0; i < nums.length; i++) {
            System.out.println(nums[i]);
        }

        return 0;
    }
}

