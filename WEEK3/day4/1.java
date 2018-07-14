import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.*;
import java.util.*;

public class Solution {
public static int[] mergeArrays(int[] myArray, int[] alicesArray) {
int[] a=new int[myArray.length + alicesArray.length];
 int i=0,j=0,k=0;
   while (i<myArray.length && j<alicesArray.length)
   {
       if(myArray[i]<alicesArray[j])
       {
           a[k]=myArray[i];
           i++;
       }
       else
       {
           a[k]=alicesArray[j];
           j++;
       }
       k++;
   }

   while(i<myArray.length)
   {
       a[k]=myArray[i];
       i++;
       k++;
   }

   while(j<alicesArray.length)
   {
       a[k]=alicesArray[j];
       j++;
       k++;
   }
   return a;
   }
 }