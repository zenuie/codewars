package com.zowda.codewars;

public class Main {

    public static int main(int s, double[] x) {
	// write your code here
        int max = 0;
        for (int i = 0; i < x.length - 1; i++) {
            max = (int) Math.max(max, (x[i + 1] - x[i]) * 3600 / s);
        }
        return max;
    }
}
