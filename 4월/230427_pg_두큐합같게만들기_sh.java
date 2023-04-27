import java.util.*;
import java.util.stream.*;
import java.lang.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = -1;
        int total_size = queue1.length + queue2.length;
        
        long sum1 = IntStream.of(queue1).sum();
        long sum2 = IntStream.of(queue2).sum();
        
        List<Integer> q1_to  = Arrays.stream(queue1).boxed().collect(Collectors.toList());
        List<Integer> q2_to  = Arrays.stream(queue2).boxed().collect(Collectors.toList());
        
        Queue<Integer> q1 = new LinkedList<Integer>(q1_to);
        Queue<Integer> q2 = new LinkedList<Integer>(q2_to);
        
        long mid = (sum1 + sum2) / 2; 
        
        if ((sum1 + sum2) % 2 != 0){
            return -1;
        }
        
        int cnt = 0;
        int temp1 = 0;
        int temp2 = 0;
        
        // 여기에서 total size 로 while 돌리면 반례 있음 (테케 1번 통과 x)
        // queue1 = {1, 1, 1, 8, 10, 9}
        // queue2 = {1, 1, 1, 1, 1, 1}
        // while 횟수 : 14번
        while(cnt <= total_size * 2){
            if (sum1 == sum2){
                break;
            }
            
            if (sum1 > mid){
                temp1 = q1.remove();
                sum1 -= temp1;
                q2.add(temp1);
                sum2 += temp1;
                cnt++;
            } else if (sum2 > mid){
                temp2 = q2.remove();
                
                sum2 -= temp2;
                q1.add(temp2);
                sum1 += temp2;
                cnt++;
            }
            
        }
        
        if (cnt > total_size && sum1 != sum2 ){
            answer = -1;
        } else{
            answer = cnt;
        }
        
        return answer;
    }
}