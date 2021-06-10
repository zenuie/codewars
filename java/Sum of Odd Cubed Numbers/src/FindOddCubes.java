public class FindOddCubes {
    public static int cubeOdd(int arr[]) {
    int result = 0;
        for(int num:arr){
            if(num%2 != 0){
                result+=num*num*num;
            }
        }

        return result;
    }
}