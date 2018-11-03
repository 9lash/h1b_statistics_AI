import os
import csv

var_status = None
var_socname = None
var_state = None

def checkcolumns(inputfile):
	if(os.path.exists(inputfile)):
		with open(inputfile) as csv_file: 
			csv_reader = csv.DictReader(csv_file, delimiter=';')
			for head in csv_reader.fieldnames:
				if(head == "STATUS"):
					var_status = "STATUS"
				elif (head == "CASE_STATUS"):
					var_status = "CASE_STATUS"
				if(head == "LCA_CASE_SOC_NAME"):
					var_socname = "LCA_CASE_SOC_NAME"
				elif(head == "SOC_NAME"):
					var_socname = "SOC_NAME"
				if(head == "WORKSITE_STATE"):
					var_state = "WORKSITE_STATE"
				elif(head == "LCA_CASE_WORKLOC1_STATE"):
					var_state = "LCA_CASE_WORKLOC1_STATE"
		csv_file.close()
		return(var_status, var_state, var_socname)



def makedicts(inputfile, var_status, var_socname, var_state):
	if(os.path.exists(inputfile)):
		with open(inputfile) as csv_file: 
			csv_reader = csv.DictReader(csv_file, delimiter=';')
			total_candidates =0
			total_cert = 0;
			occ_map = {}
			state_map = {}
			for line in csv_reader:	
				if(line[var_status] == "CERTIFIED" ):																									#STATUS           
					occ_map[line[var_socname]] = occ_map.get(line[var_socname], 0) + 1												#LCA_CASE_SOC_NAME
					state_map[line[var_state]] = state_map.get(line[var_state], 0) + 1								#LCA_CASE_EMPLOYER_STATE
					total_cert +=1
				total_candidates += 1			
		sorted_occ = sorted(occ_map.items(), key= lambda x:(-x[1],x[0]))									#Use generator expression to optimize (, x[0])
		sorted_state = sorted(state_map.items(), key = lambda x:(-x[1],x[0]))
		csv_file.close()	
		return sorted_occ, sorted_state, total_cert
	else:
		return None


#Inputs: 
#sorted dictionary: containing the occupation and its H1B counts / state & its H1B counts
#total certified: Total number of candidates in the input sheet who has been certified
#outputfile: the path where the output csvfile has to be generated
# str - String which helps form the header of the output file. 
#       eg: passing "LCA_CASE_SOC_NAME" helps the csvwriter make a heading row as: LCA_CASE_SOC_NAME, NUMBER_CERTIFIED_APPLICATIONS, PERCENTAGE   


def writefiles(sorted_dict, total_certified, outputfile, strn):
	with open(outputfile,'a', newline = '') as csv_file:
		csv_writer = csv.writer(csv_file, delimiter = ';')
		csv_writer.writerow([strn, "NUMBER_CERTIFIED_APPLICATIONS", "PERCENTAGE"])
		sample =0
		for key, value in sorted_dict:										#sorted(occ_map.items(), key = takethevalue, reverse = True):
			sample += 1
			percent = str(round((value/float(total_certified)*100),1)) + "%"
			csv_writer.writerow([key, value, percent])
			if(sample>=10):
				csv_file.close()
				break

