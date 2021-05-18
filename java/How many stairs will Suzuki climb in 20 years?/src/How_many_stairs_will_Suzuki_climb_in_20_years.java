public class How_many_stairs_will_Suzuki_climb_in_20_years {
    public static long stairsIn20(int[][] stairs)
    {
        int result = 0;
        for(int i = 0;i < stairs.length;i++){
            for(int j = 0;j < stairs[i].length;j++){
                result+=stairs[i][j];
            }
        }
        return result*20;
    }
}
