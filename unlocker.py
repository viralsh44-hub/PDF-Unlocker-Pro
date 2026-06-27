
import os,subprocess
class PDFUnlocker:
    def __init__(self,qpdf_path):
        self.qpdf_path=qpdf_path
    def unlock_all(self,source_folder,output_folder,password):
        os.makedirs(output_folder,exist_ok=True)
        pdfs=[f for f in os.listdir(source_folder) if f.lower().endswith(".pdf")]
        s=f=0
        for i,name in enumerate(pdfs,1):
            r=subprocess.run([self.qpdf_path,f"--password={password}","--decrypt",
                os.path.join(source_folder,name),os.path.join(output_folder,name)])
            if r.returncode==0:s+=1
            else:f+=1
            yield i,len(pdfs),name,s,f
