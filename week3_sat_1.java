public class sat_1{
	public static String fun(int a){
		String s=new String();
		for(int i=0;i<a;i++){
			s+="()";
		}
		String[] sp=new String[s.length()];
		int c=0;
		for(int j=0;j<s.length();j++){
			String h=new String();
			for(int k=0;k<s.length();k++){
				sp[j][k]=s[j];
			}
			c++
		}
		return sp
	} 
	public static void main(String[] args) {
		
	}
}