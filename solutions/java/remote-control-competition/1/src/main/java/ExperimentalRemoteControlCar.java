public class ExperimentalRemoteControlCar implements RemoteControlCar, Cloneable {
    private int distanceTravelled;
    public void drive() { distanceTravelled += 20; }
    public int getDistanceTravelled() { return distanceTravelled; }
}
