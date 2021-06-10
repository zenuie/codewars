public class Kata {
    public static String alphabetWar(String fight) {
        int right = 0;
        int left = 0;
        String[]  new_fight = fight.split("");
        for (String letter : new_fight) {
            switch (letter) {
                case "w":
                    left += 4;
                    break;
                case "p":
                    left += 3;
                    break;
                case "b":
                    left += 2;
                    break;
                case "s":
                    left += 1;
                    break;
                case "m":
                    right += 4;
                    break;
                case "q":
                    right += 3;
                    break;
                case "d":
                    right += 2;
                    break;
                case "z":
                    right += 1;
                    break;
            }
        }
        if(right> left){
            return "Right side wins!";
        }
        else if (left>right){
            return "Left side wins!";
        }
        return "Let's fight again!";

    }
}