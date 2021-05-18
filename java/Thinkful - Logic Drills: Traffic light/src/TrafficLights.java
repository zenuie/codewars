public class TrafficLights {

    public static String updateLight(String current) {
        String result = "";
        if(current.equals("green")){
            result = "yellow";
        }
        else if(current.equals("yellow")){
            result = "red";
        }
        else if(current.equals("red")){
            result = "green";
        }
        return result;
    }

}