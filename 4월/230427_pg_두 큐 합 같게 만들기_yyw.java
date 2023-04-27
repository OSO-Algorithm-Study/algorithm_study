import java.util.*;
class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int max_length = queue1.length * 3;
    
        Queue<Integer> queue_1 = new LinkedList<>();
        for (int i : queue1){
            queue_1.offer(i);
        }
        Queue<Integer> queue_2 = new LinkedList<>();
        for (int j : queue2){
            queue_2.offer(j);
        }
        
        long queue1_sum = sum(queue1);
        long queue2_sum = sum(queue2);
        
        int cnt = 0;
        while (cnt <= max_length){
            if (queue1_sum > queue2_sum){
                int tmp = queue_1.poll();
                queue_2.offer(tmp);
                queue1_sum -= tmp;
                queue2_sum += tmp;
                cnt++;
            } else if (queue1_sum < queue2_sum){
                int tmp = queue_2.poll();
                queue_1.offer(tmp);
                queue2_sum -= tmp;
                queue1_sum += tmp;
                cnt++;
            }
            if (queue1_sum == queue2_sum){
                return cnt;
            }
        }
        return -1;
    }
    
    public int sum(int[] arr){
        int sumValue = 0;
        for (int a : arr){
            sumValue += a;
        }
        return sumValue;
    }
}