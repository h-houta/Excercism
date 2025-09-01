public class JedliksToyCar {
    public int battery = 100;
    public int distance = 0;

    public static JedliksToyCar buy() {
        return new JedliksToyCar();
    }

    public String distanceDisplay() {
        return  "Driven " + distance + " meters";
    }

    public String batteryDisplay() {
        return battery > 0 ? "Battery at " + battery+ "%" : "Battery empty";
    }

    public void drive() {
        if(battery > 0){    
            distance +=20;
            battery -= 1;
        }
    }
}