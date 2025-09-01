public class Lasagna {
    // TODO: define the 'expectedMinutesInOven()' method
    	public int expectedMinutesInOven(){
        return 40;
    }
    // TODO: define the 'remainingMinutesInOven()' method
    public int remainingMinutesInOven(int minInOven){
        return expectedMinutesInOven() - minInOven;
    }
    
    // TODO: define the 'preparationTimeInMinutes()' method
    public int preparationTimeInMinutes(int lLayers){
        return lLayers * 2;
    }

    // TODO: define the 'totalTimeInMinutes()' method
    public int totalTimeInMinutes(int lLayer, int min){
        return preparationTimeInMinutes(lLayer) + min;
    }
}