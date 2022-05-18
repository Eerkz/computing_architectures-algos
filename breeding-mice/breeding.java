public class breeding {
    public static void main(String[] args){
        long startTime = System.nanoTime(); 

        //start of simulation
        int N = 6; 

        for (int i = 0; i < 18; i++){
            System.out.println("Total pairs: " + breedingSimulator(i));
        }

        long endTime = System.nanoTime();

        //end of simulation

        System.out.println("Execution time in ns: " + (endTime - startTime));
    }

    public static int breedingSimulator(int N) {
        int pair = (int) ((Math.pow(((1 + Math.sqrt(5))/2), N) - Math.pow(-((1 + Math.sqrt(5))/2), -N))/Math.sqrt(5));
        return pair;
    }
}
