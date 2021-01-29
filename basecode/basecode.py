#this file contains the base code used to get the video titles
import pytube

l = pytube.get('https://www.youtube.com/watch?v=SlPhMPnQ58k&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10')

def tv():
	self.video_urls
	self.stepend=[]
	for papersheet in self.pagesaved:
	    #chaves = re.findall(r'"title":{(.+?),',arquivo)
	    step1 = re.findall(r'"title"(.+?)}],"accessibility"',papersheet)
	    #DEIXANDO VARIAVEI BONITAS PARA PRINT
	    step1.pop()
	    step1.append('END')

	    #len(chaves)

	    step2 = 'CODE-090231@1'.join(step1)

	    step3 = re.findall(r':{"runs":\[{"text":"(.+?)"CODE-090231@1',step2)


	    # In[18]:


	    #filter private videos
	    counter = 0
	    searchFilter='"title":{"runs":[{"text":"'
	    r=0
	    for i in step3:
	        if(i.find('[Private video]')!= -1):
	            n = i.find(searchFilter)
	            r=i[n+len(searchFilter):len(i)]
	            print(r)
	            self.stepend.append('[Private Video]')
	            self.stepend.append(r)
	        elif(i.find('[Deleted video]')!= -1):
	            n = i.find(searchFilter)
	            r=i[n+len(searchFilter):len(i)]
	            print(r)
	            self.stepend.append('[Deleted Video]')
	            self.stepend.append(r)
	        else:
	            self.stepend.append(i)


	return self.stepend