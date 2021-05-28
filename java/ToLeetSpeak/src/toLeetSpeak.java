import java.lang.*;
class Kata {
    static String toLeetSpeak(final String speak) {
        StringBuilder result = new StringBuilder();
        for(int i = 0;i < speak.length();i++){

            switch (speak.substring(i, i + 1)) {
                case "A" -> result.append("@");
                case "B" -> result.append("8");
                case "C" -> result.append("(");
                case "E" -> result.append("3");
                case "G" -> result.append("6");
                case "H" -> result.append("#");
                case "I" -> result.append("!");
                case "L" -> result.append("1");
                case "O" -> result.append("0");
                case "S" -> result.append("$");
                case "T" -> result.append("7");
                case "Z" -> result.append("2");
                default -> result.append(speak.charAt(i));
            }
        }
        return result.toString();
    }
}