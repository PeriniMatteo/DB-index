###!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
dbname="indexdb"
P=True
try:
    con = mdb.connect('localhost', 'indexroot', 'index0', 'indexdb');
        
    cur = con.cursor()
    cur.execute("DROP DATABASE indexdb;")
    cur.execute("CREATE DATABASE indexdb;")
    #CREATE COUNTRIES TABLE
    #cur.execute("DROP TABLE IF EXISTS Countries")
    cur.execute("CREATE TABLE IF NOT EXISTS `"+dbname+"`.`Countries` (\
    `idCountries` INT NOT NULL AUTO_INCREMENT COMMENT '',\
    `Common_name` VARCHAR(50) NOT NULL COMMENT '',\
    `Formal_name` VARCHAR(80) NOT NULL COMMENT '',\
    `Capital` VARCHAR(45) NOT NULL COMMENT '',\
    `ISO_2_Letter_Code` VARCHAR(2) NOT NULL COMMENT '',\
    `ISO_3_Letter_Code` VARCHAR(3) NOT NULL COMMENT '',\
    PRIMARY KEY (`idCountries`)  COMMENT '')\
    ENGINE = InnoDB")
    
    #CREATE ARTICLES TABLE
    #cur.execute("DROP TABLE IF EXISTS Articles")
    cur.execute("CREATE TABLE IF NOT EXISTS `"+dbname+"`.`Articles` (\
    `idArticles` INT NOT NULL AUTO_INCREMENT COMMENT '',\
    `Article_number` DECIMAL(3,1) NOT NULL COMMENT '',\
    `Article_Field` MEDIUMTEXT NOT NULL COMMENT '',\
    `Article_text` MEDIUMTEXT NOT NULL COMMENT '',\
    PRIMARY KEY (`idArticles`)  COMMENT '',\
    UNIQUE INDEX `idArticols_UNIQUE` (`idArticles` ASC)  COMMENT '',\
    UNIQUE INDEX `Article_number_UNIQUE` (`Article_number` ASC)  COMMENT '')\
    ENGINE = InnoDB")
    
    #CREATE QUESTIONS TABLE
    #cur.execute("DROP TABLE IF EXISTS Questions")
    cur.execute("CREATE TABLE IF NOT EXISTS `"+dbname+"`.`Questions` (\
    `idQuestions` INT NOT NULL AUTO_INCREMENT COMMENT '',\
    `Question_section` VARCHAR(45) NOT NULL COMMENT '',\
    `Question_number` VARCHAR(45) NOT NULL COMMENT '',\
    `Question_text` MEDIUMTEXT NOT NULL COMMENT '',\
    `Articles_idArticles` INT NOT NULL COMMENT '',\
    PRIMARY KEY (`idQuestions`, `Articles_idArticles`)  COMMENT '',\
    INDEX `fk_Questions_Articles1_idx` (`Articles_idArticles` ASC)  COMMENT '',\
    CONSTRAINT `fk_Questions_Articles1`\
    FOREIGN KEY (`Articles_idArticles`)\
    REFERENCES `"+dbname+"`.`Articles` (`idArticles`)\
    ON DELETE NO ACTION\
    ON UPDATE NO ACTION)\
    ENGINE = InnoDB")
    
    #CREATE ASSESMENT TABLE
    #cur.execute("DROP TABLE IF EXISTS Assesment")
    cur.execute("CREATE TABLE IF NOT EXISTS `"+dbname+"`.`Assesment` (\
    `idAssesment` INT NOT NULL AUTO_INCREMENT COMMENT '',\
    `Assesment_Name` VARCHAR(45) NOT NULL COMMENT '',\
    `Assesment_Description` MEDIUMTEXT COMMENT '',\
    PRIMARY KEY (`idAssesment`)  COMMENT '',\
    UNIQUE INDEX `Assesment_Name_UNIQUE` (`Assesment_Name` ASC)  COMMENT '',\
    UNIQUE INDEX `idAssesment_UNIQUE` (`idAssesment` ASC)  COMMENT '')\
    ENGINE = InnoDB")
    
    #CREATE QUESTION IN ASSESMENT TABLE
    #cur.execute("DROP TABLE IF EXISTS QuestionInAssesment")
    cur.execute("CREATE TABLE IF NOT EXISTS `"+dbname+"`.`QuestionInAssesment` (\
    `idQIA` INT NOT NULL AUTO_INCREMENT COMMENT '',\
    `Assesment_idAssesment` INT NOT NULL COMMENT '',\
    `Questions_idQuestions` INT NOT NULL COMMENT '',\
    PRIMARY KEY (`idQIA`, `Assesment_idAssesment`, `Questions_idQuestions`)  COMMENT '',\
    INDEX `fk_QuestionInAssesment_Assesment1_idx` (`Assesment_idAssesment` ASC)  COMMENT '',\
    INDEX `fk_QuestionInAssesment_Questions1_idx` (`Questions_idQuestions` ASC)  COMMENT '',\
    CONSTRAINT `fk_QuestionInAssesment_Assesment1`\
    FOREIGN KEY (`Assesment_idAssesment`)\
    REFERENCES `"+dbname+"`.`Assesment` (`idAssesment`)\
    ON DELETE NO ACTION\
    ON UPDATE NO ACTION,\
    CONSTRAINT `fk_QuestionInAssesment_Questions1`\
    FOREIGN KEY (`Questions_idQuestions`)\
    REFERENCES `"+dbname+"`.`Questions` (`idQuestions`)\
    ON DELETE NO ACTION\
    ON UPDATE NO ACTION)\
    ENGINE = InnoDB")
    
    #CREATE INQUIRIES TABLE
    #cur.execute("DROP TABLE IF EXISTS Inquries")
    cur.execute("CREATE TABLE IF NOT EXISTS `"+dbname+"`.`Inquiries` (\
    `idInquiries` INT NOT NULL AUTO_INCREMENT COMMENT '',\
    `Inquiry_name` VARCHAR(45) NOT NULL COMMENT '',\
    `Inquiry_description` MEDIUMTEXT NULL COMMENT '',\
    `Inquiry_date` DATE NOT NULL COMMENT '',\
    `Countries_idCountries` INT NOT NULL COMMENT '',\
    PRIMARY KEY (`idInquiries`, `Countries_idCountries`)  COMMENT '',\
    UNIQUE INDEX `idInquiries_UNIQUE` (`idInquiries` ASC)  COMMENT '',\
    UNIQUE INDEX `Inquiry_name_UNIQUE` (`Inquiry_name` ASC)  COMMENT '',\
    INDEX `fk_Inquiries_Countries1_idx` (`Countries_idCountries` ASC)  COMMENT '',\
    CONSTRAINT `fk_Inquiries_Countries1`\
    FOREIGN KEY (`Countries_idCountries`)\
    REFERENCES `"+dbname+"`.`Countries` (`idCountries`)\
    ON DELETE NO ACTION\
    ON UPDATE NO ACTION)\
    ENGINE = InnoDB")
    
    #CREATE ANSWERS TABLE
    #cur.execute("DROP TABLE IF EXISTS Answers")
    cur.execute("CREATE TABLE IF NOT EXISTS `"+dbname+"`.`Answers` (\
    `idAnswers` INT NOT NULL AUTO_INCREMENT COMMENT '',\
    `Answere_Details` LONGTEXT NULL COMMENT '',\
    `Score_Details` VARCHAR(45) NOT NULL COMMENT '',\
    `Answere_Score` DECIMAL(5,3) NOT NULL COMMENT '',\
    `Inquiries_idInquiries` INT NOT NULL COMMENT '',\
    `QuestionInAssesment_idQIA` INT NOT NULL COMMENT '',\
    PRIMARY KEY (`idAnswers`, `Inquiries_idInquiries`, `QuestionInAssesment_idQIA`)  COMMENT '',\
    INDEX `fk_Answers_Inquiries_idx` (`Inquiries_idInquiries` ASC)  COMMENT '',\
    INDEX `fk_Answers_QuestionInAssesment1_idx` (`QuestionInAssesment_idQIA` ASC)  COMMENT '',\
    CONSTRAINT `fk_Answers_Inquiries`\
    FOREIGN KEY (`Inquiries_idInquiries`)\
    REFERENCES `"+dbname+"`.`Inquiries` (`idInquiries`)\
    ON DELETE NO ACTION\
    ON UPDATE NO ACTION,\
    CONSTRAINT `fk_Answers_QuestionInAssesment1`\
    FOREIGN KEY (`QuestionInAssesment_idQIA`)\
    REFERENCES `"+dbname+"`.`QuestionInAssesment` (`idQIA`)\
    ON DELETE NO ACTION\
    ON UPDATE NO ACTION)\
    ENGINE = InnoDB")
    
    
    if P:
        #####Populate Articles
        f=open("Articles.csv")
        for r in f.readlines():
            rr=r.strip('\n').split(';')
            cur.execute("INSERT INTO `"+dbname+"`.`Articles` (`Article_number`, `Article_Field`, `Article_text`) VALUES ('"+rr[0]+"', '"+rr[1]+"', '"+rr[2]+"');")
            f.close()
        con.commit()
        
    if P:
        #####Populate Assesment
        f=open("Assesment.csv")
        for r in f.readlines():
            rr=r.strip('\n').split(';')
            cur.execute("INSERT INTO `"+dbname+"`.`Assesment` (`Assesment_Name`, `Assesment_Description`) VALUES ('"+rr[0]+"', '"+rr[1]+"');")
            f.close()
        con.commit()
        
    if P:
        #####Populate Countries
        f=open("Countries.csv")
        for r in f.readlines():
            rr=r.strip('\n').split(';')
            cur.execute("INSERT INTO `"+dbname+"`.`Countries` (`Common_name`, `Formal_name`, `Capital`, `ISO_2_Letter_Code`, `ISO_3_Letter_Code`) VALUES ("+str("'"+rr[0]+"'")+","+str("'"+rr[1]+"'")+","+str("'"+rr[2]+"'")+","+str("'"+rr[3]+"'")+","+str("'"+rr[4]+"'")+");")
            f.close()
        con.commit()
    
    if P:
         #####Populate Questions
        f=open("Questions.csv")
        for r in f.readlines():
            rr=r.strip('\n').split(';')
            cur.execute("SELECT idArticles FROM indexdb.Articles where Article_number="+str(rr[3])+";")
            idArticles=cur.fetchone()
            cur.execute("INSERT INTO `"+dbname+"`.`Questions` (`Question_section`, `Question_number`, `Question_text`, `Articles_idArticles`) VALUES ('"+rr[0]+"', '"+rr[1]+"', '"+rr[2]+"','"+str(idArticles[0])+"'"+");")
            f.close()
        con.commit()
            
    if P:
        ###############################################################
        ##########                                           ##########
        ##########               WARNING!!!                  ##########
        ##########                                           ##########
        ###############################################################
        #                  ONLY IN THIS CASE!!!!!!!!!!!!!!
        
        #####Populate QuestionInAssesment
        #f=open("Questions.csv")
        #for r in f.readlines():
        #rr=r.strip('\n').split(';')
        cur.execute("SELECT idQuestions FROM indexdb.Questions")
        for Question in cur.fetchall():

            cur.execute("INSERT INTO `"+dbname+"`.`QuestionInAssesment` (`Assesment_idAssesment`, `Questions_idQuestions`) VALUES ('1','"+str(Question[0])+"');")
        con.commit()
    
    if P:
        #####Populate Inquiries
        #f=open("Inquiries.csv")
        #for r in f.readlines():
        #    rr=r.strip('\n').split(';')
        cur.execute("INSERT INTO `"+dbname+"`.`Inquiries` (`Inquiry_name`, `Inquiry_description`, `Inquiry_date`, `Countries_idCountries`) VALUES ('Romania2015', '','2015/03/02','141');")
        cur.execute("INSERT INTO `"+dbname+"`.`Inquiries` (`Inquiry_name`, `Inquiry_description`, `Inquiry_date`, `Countries_idCountries`) VALUES ('Moldova2015', '', '2015/09/22','114');")
        cur.execute("INSERT INTO `"+dbname+"`.`Inquiries` (`Inquiry_name`, `Inquiry_description`, `Inquiry_date`, `Countries_idCountries`) VALUES ('Serbia2015','','2015/07/14','152');")
        cur.execute("INSERT INTO `"+dbname+"`.`Inquiries` (`Inquiry_name`, `Inquiry_description`, `Inquiry_date`, `Countries_idCountries`) VALUES ('Georgia2015','','2015/01/01','63');")
        
        con.commit()
        
    if P:
        #####Populate Answers Romania
        f=open("AnswersRO.csv")
        cur.execute("SELECT idInquiries FROM indexdb.Inquiries where Inquiry_name='Romania2015';")
        idInquiries=cur.fetchone()
        #print idInquiries
        for r in f.readlines():
            rr=r.strip('\n').split(';')
            #print rr
            cur.execute("SELECT idQIA, Assesment_idAssesment, Questions_idQuestions, Question_section, Question_number, Assesment_Name, Articles_idArticles, idArticles,Article_number, Article_Field\
            FROM indexdb.QuestionInAssesment, indexdb.Questions, indexdb.Assesment, indexdb.Articles\
            WHERE Article_number="+rr[2]+" and Question_number="+rr[1]+" and Question_section='"+rr[0]+"' and Articles_idArticles=idArticles and idQuestions=Questions_idQuestions;")
            idQIA=cur.fetchone()
            #print idInquiries[0], idQIA[0]
            #print rr[3],rr[4],rr[5]
            #print "INSERT INTO `"+dbname+"`.`Answers` (`Answere_Details`, `Score_Details`, `Answere_Score`, `Inquiries_idInquiries`, `QuestionInAssesment_idQIA`) VALUES ('"+rr[3]+"', '"+rr[4]+"', '"+str(float(rr[5]))+"','"+str(int(idQIA[0]))+"', '"+str(int(idInquiries[0]))+"');"
            cur.execute("INSERT INTO `"+dbname+"`.`Answers` (`Answere_Details`, `Score_Details`, `Answere_Score`, `Inquiries_idInquiries`, `QuestionInAssesment_idQIA`) VALUES ('"+rr[3].replace("'",'')+"', '"+rr[4]+"', '"+str(float(rr[5].replace(',','.')))+"', '"+str(int(idInquiries[0]))+"','"+str(int(idQIA[0]))+"');")
            #print "a"
        con.commit()
    
    if P:
        #####Populate Answers Moldova
        f=open("AnswersMO.csv")
        cur.execute("SELECT idInquiries FROM indexdb.Inquiries where Inquiry_name='Moldova2015';")
        idInquiries=cur.fetchone()
        #print idInquiries
        for r in f.readlines():
            rr=r.strip('\n').split(';')
            #print rr
            cur.execute("SELECT idQIA, Assesment_idAssesment, Questions_idQuestions, Question_section, Question_number, Assesment_Name, Articles_idArticles, idArticles,Article_number, Article_Field\
            FROM indexdb.QuestionInAssesment, indexdb.Questions, indexdb.Assesment, indexdb.Articles\
            WHERE Article_number="+rr[2].replace(',','.')+" and Question_number="+rr[1]+" and Question_section='"+rr[0]+"' and Articles_idArticles=idArticles and idQuestions=Questions_idQuestions;")
            idQIA=cur.fetchone()
            #print idInquiries[0], idQIA[0]
            #print rr[3],rr[4],rr[5]
            #if idQIA[0]==468:
                #print "INSERT INTO `"+dbname+"`.`Answers` (`Answere_Details`, `Score_Details`, `Answere_Score`, `Inquiries_idInquiries`, `QuestionInAssesment_idQIA`) VALUES ('"+rr[3]+"', '"+rr[4]+"', '"+str(float(rr[5]))+"','"+str(int(idQIA[0]))+"', '"+str(int(idInquiries[0]))+"');"
            cur.execute("INSERT INTO `"+dbname+"`.`Answers` (`Answere_Details`, `Score_Details`, `Answere_Score`, `Inquiries_idInquiries`, `QuestionInAssesment_idQIA`) VALUES ('"+rr[3].replace("'",'')+"', '"+rr[4]+"', '"+str(float(rr[5].replace(',','.')))+"', '"+str(int(idInquiries[0]))+"','"+str(int(idQIA[0]))+"');")
            #print "a"
        con.commit()
        

    if P:
        #####Populate Answers Serbia
        f=open("AnswersRS.csv")
        cur.execute("SELECT idInquiries FROM indexdb.Inquiries where Inquiry_name='Serbia2015';")
        idInquiries=cur.fetchone()
        #print idInquiries
        for r in f.readlines():
            rr=r.strip('\n').split(';')
            #print rr
            cur.execute("SELECT idQIA, Assesment_idAssesment, Questions_idQuestions, Question_section, Question_number, Assesment_Name, Articles_idArticles, idArticles,Article_number, Article_Field\
            FROM indexdb.QuestionInAssesment, indexdb.Questions, indexdb.Assesment, indexdb.Articles\
            WHERE Article_number="+rr[2].replace(',','.')+" and Question_number="+rr[1]+" and Question_section='"+rr[0]+"' and Articles_idArticles=idArticles and idQuestions=Questions_idQuestions;")
            idQIA=cur.fetchone()
            cur.execute("INSERT INTO `"+dbname+"`.`Answers` (`Answere_Details`, `Score_Details`, `Answere_Score`, `Inquiries_idInquiries`, `QuestionInAssesment_idQIA`) VALUES ('"+rr[3].replace("'",'')+"', '"+rr[4]+"', '"+str(float(rr[5].replace(',','.')))+"', '"+str(int(idInquiries[0]))+"','"+str(int(idQIA[0]))+"');")
            #print "a"
        con.commit()


    if P:
        #####Populate Answers Georgia
        f=open("AnswersGE.csv")
        cur.execute("SELECT idInquiries FROM indexdb.Inquiries where Inquiry_name='Georgia2015';")
        idInquiries=cur.fetchone()
        for r in f.readlines():
            rr=r.strip('\n').split(';')
            cur.execute("SELECT idQIA, Assesment_idAssesment, Questions_idQuestions, Question_section, Question_number, Assesment_Name, Articles_idArticles, idArticles,Article_number, Article_Field\
            FROM indexdb.QuestionInAssesment, indexdb.Questions, indexdb.Assesment, indexdb.Articles\
            WHERE Article_number="+rr[2].replace(',','.')+" and Question_number="+rr[1]+" and Question_section='"+rr[0]+"' and Articles_idArticles=idArticles and idQuestions=Questions_idQuestions;")
            idQIA=cur.fetchone()
            cur.execute("INSERT INTO `"+dbname+"`.`Answers` (`Answere_Details`, `Score_Details`, `Answere_Score`, `Inquiries_idInquiries`, `QuestionInAssesment_idQIA`) VALUES ('"+rr[3].replace("'",'')+"', '"+rr[4]+"', '"+str(float(rr[5].replace(',','.')))+"', '"+str(int(idInquiries[0]))+"','"+str(int(idQIA[0]))+"');")
        con.commit()

except mdb.Error, e:
  
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
finally:    
        
    if con:    
        con.close()
