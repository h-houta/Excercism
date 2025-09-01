public class ProductionRemoteControlCar implements RemoteControlCar, Comparable<ProductionRemoteControlCar> {
    private int numberOfVictories;
    private int distanceTravelled;
    public void setNumberOfVictories(int numberOfVictories) { this.numberOfVictories = numberOfVictories; }
    public int getNumberOfVictories() { return numberOfVictories;}
    @Override
    public void drive() { distanceTravelled += 10; }
    @Override
    public int getDistanceTravelled() { return distanceTravelled; }
    @Override
    public int compareTo(ProductionRemoteControlCar other) { return Integer.compare(other.numberOfVictories, this.numberOfVictories); }
}