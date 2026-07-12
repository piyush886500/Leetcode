import java.util.HashMap;
class Prob_13{
    public static void main(String[] args) {
        HashMap<Character, Integer> letters = new HashMap<>();
        String s = "MCMXCIV";
        int n = s.length();
        int result = 0;
            letters.put('I',1);
            letters.put('V',5);
            letters.put('X',10);
            letters.put('L',50);
            letters.put('C',100);
            letters.put('D',500);
            letters.put('M',1000);
            // System.out.println(letters.get(s.charAt(3)));

            for(int i=0;i<n;i++){
                // int  val = letters.get(s.charAt(i));
                // int  val1 = letters.get(s.charAt(i+1));
                if(i<n-1 && letters.get(s.charAt(i))<letters.get(s.charAt(i+1))){
                    result-=letters.get(s.charAt(i));
                }
                else{
                    result+=letters.get(s.charAt(i));
                }
            }
            System.out.println(result);
    }

}