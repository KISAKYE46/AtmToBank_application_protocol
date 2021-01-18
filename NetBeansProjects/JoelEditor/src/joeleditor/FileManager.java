/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package joeleditor;

/**
 *
 * @author kisakye
 */
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import javax.swing.JFileChooser;
public class FileManager {
    
    
    public String readFile(File f)throws IOException{
        FileReader fr = new FileReader(f);
        
        int i = fr.read();
        String data = "";
        
        while(i!=-1){
           data = data+(char)i;
           i=fr.read();
        
        }
        
        fr.close();
        
        return data;
    }
    
    public File openFile()throws IOException{
    
    JFileChooser fc  = new JFileChooser();
    
    int dir = fc.showOpenDialog(null);
    
    if(dir==JFileChooser.APPROVE_OPTION){
       File f =  fc.getSelectedFile();
       
       return f;
    
    }else{
    
        return null;
    
    }
    
    }
    
    public File save(File dir,String data) throws IOException{
        
    if(dir!=null){
     if(!dir.exists()){
            dir.createNewFile();
        }
        FileWriter fw = new FileWriter(dir);
        fw.write(data);
        fw.flush();
        fw.close();
        return dir;
       
    }else{
       return  saveAs(data);
    
    }
   
    
    }
    
    public File saveAs(String data)throws IOException{
    JFileChooser fc = new JFileChooser();
    int result = fc.showSaveDialog(null);
   
    if(result==JFileChooser.APPROVE_OPTION){
    File f = fc.getSelectedFile();
    
    if(!f.exists()){
            f.createNewFile();
        }
        FileWriter fw = new FileWriter(f);
        fw.write(data);
        fw.flush();
        fw.close();
        
        return f;
    
    }
    
    return null;
        
        
        
    }
    
    
    public static void main(String[] args) throws IOException{
            //
    }
            
    
}
