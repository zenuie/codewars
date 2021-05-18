

public class Movie {

    public static int movie(int card, int ticket, double perc) {
        int num = 0;
        int priceA = 0;
        double priceB = card;

        while (Math.ceil(priceB) >= priceA) {
            num += 1;
            priceA += ticket;
            double pow = Math.pow(perc, num);
            priceB += ticket * pow;
        }
        return num;
    }
}