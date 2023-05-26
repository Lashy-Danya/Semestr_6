/*****************************************************************************
 Помощь в выборе игры
******************************************************************************/
include "logic_es_win.inc"
include "logic_es_win.con"
include "hlptopic.con"

%BEGIN_WIN Task Window
/***************************************************************************
		Event handling for Task Window
***************************************************************************/
predicates
  task_win_eh : EHANDLER
     rev(char_list,char_list,char_list).
     reverse(char_list,char_list).
     nondeterm rule(rule_number,category,category,conditions)
     nondeterm cond(cond_number,condition)
     nondeterm topic(condition)
     assert_database
     do_consulting
     nondeterm info
     erase
     clear
     do_answer(cond_number,integer)
     keyword(category)
     first_keyword_in_sentence(word_list,category)
     member(char,char_list).
     nondeterm symbol_counter(string,integer).
     nondeterm del_front_space(string,string).
     nondeterm fronttoken_cyr(string,string,string).
     nondeterm convers(string,word_list)
     nondeterm upper_lower_cyr(string,string).
     nondeterm upper_lower_cyr_convers(char_list,char_list).
     nondeterm str_char_list(string,char_list).
     pack(char_list,string).
     goes(string,category)
     nondeterm go(history,category)
     nondeterm check(rule_number,history,conditions)
     ask_question(cond_number,condition)

constants

%BEGIN Task Window, CreateParms, 21:26:22-22.12.2007, Code automatically updated!
  task_win_Flags = [wsf_SizeBorder,wsf_TitleBar,wsf_Close,wsf_Maximize,wsf_Minimize,wsf_ClipSiblings]
  task_win_Menu  = res_menu(idr_task_menu)
  task_win_Title = "Экспертная система, базирующаяся на логике"
  task_win_Help  = idh_contents
%END Task Window, CreateParms

clauses
/* База знаний. */

/* Размещение в резидентной БД информации из утверждений БЗ ЭС */
     assert_database:-
           rule(Rule_number,Category,Type_of_breed,Conditions),
           assertz(d_rule(Rule_number,Category,Type_of_breed,Conditions)),fail.
     assert_database:-
           cond(Cond_number,Condition),
          assertz(d_cond(Cond_number,Condition)),fail.
     assert_database:-
           topic(Condition),
           assertz(d_topic(Condition)),fail.

     assert_database:-!.
/* Условия-характеристики различных игр.*/
     cond(1,"однопользовательская").
     cond(2,"многопользовательская").
     cond(3,"Цена до 500 руб").
     cond(4,"Цена до 1000 руб").
     cond(5,"Конечная цель").
     cond(6,"Вид от третьего лица").
     cond(7,"Вид от первого лица").
     cond(8,"Вид сверху").
     cond(9,"Есть боевая система").
     cond(10,"Есть экономическая система").
     cond(11,"Открытый мир").
     cond(12,"Пошаговое течение времени").
     cond(13,"Реалистичная физика").
     cond(14,"Кооператив").
/* Данные о типах игр */
     topic("однопользовательская").
     topic("многопользовательская").
/* Данные о конкретных играх */
     rule(1,"Игра","однопользовательская",[1]).
     rule(2,"Игра","многопользовательская",[2]).
     rule(3,"однопользовательская","The Witcher",[3,5,6,9,11]).
     rule(4,"однопользовательская","Dying Light",[4,5,7,9,11]).
     rule(5,"однопользовательская","Warcraft 3",[3,8,10,9]).
     rule(6,"однопользовательская","XCOM: Enemy Unknown",[3,5,8,9,12]).
     rule(7,"однопользовательская","Half-Life: Alyx",[4,5,7,9,13]).
     rule(8,"однопользовательская","Battle Brothers",[3,8,9,10,12]).
     rule(9,"многопользовательская","Left 4 Dead",[3,7,9,14]).
     rule(10,"многопользовательская","Rust",[4,7,9,11]).
     rule(11,"многопользовательская","Warhammer: Vermintide",[3,7,9,10,14]).
     rule(12,"многопользовательская","Northgard",[3,8,9,10,14]).
     rule(13,"многопользовательская","SpellForce 3",[4,8,9,10,14]).
     rule(14,"многопользовательская","Divinity: Original Sin",[4,5,8,9,10,14]).
     do_consulting:-
           goes(_,First_keyword),
           go([],First_keyword),!.
     do_consulting:-
           not(dummy),
           dlg_Error("Информация об интересующей Вас игре отсутствует в базе знаний."),
           clear.  
/* Выдача подсказки */
     info:-
           findall(Breed_type,topic(Breed_type),Breed_type_list),
           term_str(slist,Breed_type_list,Breed_type_list_str_repr),
           str_char_list(Breed_type_list_str_repr,[_|Breed_type_list_char_repr]),
           reverse(Breed_type_list_char_repr,[_|Breed_type_list_char_repr_rev]),
           reverse(Breed_type_list_char_repr_rev,Breed_type_list_char_repr_rev1),
           pack(Breed_type_list_char_repr_rev1,Breed_type_list_str_repr1),
           dlg_Note("База знаний содержит информацию об играх типа: ",Breed_type_list_str_repr1),
           assertz(dummy).
/* Запрос и получение ответов yes и no от пользователя */
     ask_question(Breed_cond,Text):-
           concat("Вопрос : ",Text,Temp),
           concat(Temp," ",Temp1),
           concat(Temp1,"?",Quest),
           Response1=dlg_Ask("Консультация",Quest,["Да","Нет"]),
           Response=Response1+1,
           do_answer(Breed_cond,Response).

/* Предикаты ЕЯ-интерфейса */
/* Реверсирование списка */
     rev([],Init,Init).
     rev([H|T],Init,Res):-
        rev(T,[H|Init],Res).
        
     reverse(Arg,Res):-
        rev(Arg,[],Res).
/* Принадлежность элемента списку */
     member(Head,[Head|_]):-!.
     member(Elem,[_|T]):-
             member(Elem,T).
/* Подсчет символов в строке до конца строки, либо ближайшего пробела,
   символа возврата каретки, перевода строки, !,",#,$ */
     symbol_counter(Str,0):-
             frontchar(Str,'\32',_),!.
     symbol_counter(Str,0):-
             frontchar(Str,'\10',_),!.
     symbol_counter(Str,0):-
             frontchar(Str,'\13',_),!.
     symbol_counter(Str,0):-
             frontchar(Str,'\33',_),!.
     symbol_counter(Str,0):-
             frontchar(Str,'\34',_),!.
     symbol_counter(Str,0):-
             frontchar(Str,'\35',_),!.
     symbol_counter(Str,0):-
             frontchar(Str,'\36',_),!.
     symbol_counter(Str,0):-
             frontchar(Str,'\40',_),!.
     symbol_counter(Str,0):-
             frontchar(Str,'\41',_),!.
     symbol_counter(Str,0):-
             frontchar(Str,'\44',_),!.
     symbol_counter(Str,0):-
             frontchar(Str,'\45',_),!.
     symbol_counter(Str,0):-
             frontchar(Str,'\46',_),!.
     symbol_counter(Str,0):-
             frontchar(Str,'\59',_),!.
     symbol_counter("",0).
     symbol_counter(Str,Number):-
             frontchar(Str,_Char,Rest_of_string),
             symbol_counter(Rest_of_string,Number1),
             Number=Number1+1.
/* Выделение подстроки до первого разделителя */
     fronttoken_cyr(Str,Token,Rest_of_string):-
             symbol_counter(Str,Number),
             frontstr(Number,Str,Token,Rest_of_string).
/* Удаление разделителя в начале строки */
     del_front_space("","").
     del_front_space(Arg,Res):-
             frontchar(Arg,Char,Res1),Char='\32',!,
             del_front_space(Res1,Res).
     del_front_space(Arg,Res):-
             frontchar(Arg,Char,Res1),Char='\10',!,
             del_front_space(Res1,Res).
     del_front_space(Arg,Res):-
             frontchar(Arg,Char,Res1),Char='\13',!,
             del_front_space(Res1,Res).
     del_front_space(Arg,Res):-
             frontchar(Arg,Char,Res1),Char='\33',!,
             del_front_space(Res1,Res).
     del_front_space(Arg,Res):-
             frontchar(Arg,Char,Res1),Char='\34',!,
             del_front_space(Res1,Res).
     del_front_space(Arg,Res):-
             frontchar(Arg,Char,Res1),Char='\35',!,
             del_front_space(Res1,Res).
     del_front_space(Arg,Res):-
             frontchar(Arg,Char,Res1),Char='\36',!,
             del_front_space(Res1,Res).
     del_front_space(Arg,Res):-
             frontchar(Arg,Char,Res1),Char='\44',!,
             del_front_space(Res1,Res).
     del_front_space(Arg,Res):-
             frontchar(Arg,Char,Res1),Char='\40',!,
             del_front_space(Res1,Res).
     del_front_space(Arg,Res):-
             frontchar(Arg,Char,Res1),Char='\41',!,
             del_front_space(Res1,Res).
     del_front_space(Arg,Res):-
             frontchar(Arg,Char,Res1),Char='\45',!,
             del_front_space(Res1,Res).
     del_front_space(Arg,Res):-
             frontchar(Arg,Char,Res1),Char='\46',!,
             del_front_space(Res1,Res).
     del_front_space(Arg,Res):-
             frontchar(Arg,Char,Res1),Char='\59',!,
             del_front_space(Res1,Res).
     del_front_space(Arg,Arg):-frontchar(Arg,Char,_),
                               not(member(Char,['\32','\10','\13','\33',
                                                '\34','\35','\36','\40','\41',
                                                '\44','\45','\46','\59'])).
/* Правило преобразования строки в список слов */
     convers("",[]):-!.
     convers(Str,[Head1|Tail]):-
             fronttoken_cyr(Str,Head,Str2),
             upper_lower_cyr(Head,Head1),
             del_front_space(Str2,Str1),
             convers(Str1,Tail).
/* Предикат upper_lower для кирилицы Windows */
     upper_lower_cyr(InString,OutString):-
             str_char_list(InString,Char_List_for_InString),
             upper_lower_cyr_convers(Char_List_for_InString,Char_List_for_OutString),
             pack(Char_List_for_OutString,OutString).
     upper_lower_cyr_convers([],[]).
     upper_lower_cyr_convers([Char|Char_List],[Char1|Char_List1]):-
             char_int(Char,ASCII_code),
             ASCII_code>=192,ASCII_code<=223,!,
             ASCII_code_new=ASCII_code+32,
             char_int(Char1,ASCII_code_new),
             upper_lower_cyr_convers(Char_List,Char_List1).
     upper_lower_cyr_convers([Char|Char_List],[Char1|Char_List1]):-
             char_int(Char,ASCII_code),
             ASCII_code=168,!,
             ASCII_code_new=ASCII_code+16,
             char_int(Char1,ASCII_code_new),
             upper_lower_cyr_convers(Char_List,Char_List1).
     upper_lower_cyr_convers([Char|Char_List],[Char1|Char_List1]):-
             char_int(Char,ASCII_code),
             ASCII_code>=65,ASCII_code<=90,!,
             ASCII_code_new=ASCII_code+32,
             char_int(Char1,ASCII_code_new),
             upper_lower_cyr_convers(Char_List,Char_List1).
     upper_lower_cyr_convers([Char|Char_List],[Char|Char_List1]):-
             upper_lower_cyr_convers(Char_List,Char_List1).
/* Преобразование строки в список символов */
     str_char_list("",[]).
     str_char_list(Word,[Char|Char_List]):-
             frontchar(Word,Char,WordRest),
             str_char_list(WordRest,Char_List).
/* Превращение списка символов в строку */
     pack([],"").
     pack([H|T],Res):-
             str_char(Str_H,H),
             pack(T,Res1),
             concat(Str_H,Res1,Res).
/* Проверка правильности ключевого слова */
     keyword(Keyword):-
             rule(_,Keyword,_,_),!.
     keyword(Keyword):-
             rule(_,_,Keyword,_),!.
/* Поиск первого ключевого слова в высказывании пользователя */
     first_keyword_in_sentence([Head|_],Head):-
             keyword(Head),!.
     first_keyword_in_sentence([_|Tail],First_keyword):-
             first_keyword_in_sentence(Tail,First_keyword).
     first_keyword_in_sentence([],_):-!,info,fail.
/* Ввод запроса на естественном (русском) языке */
     goes(Mygoal,First_keyword):-
           Mygoal=dlg_GetStr("Консультация","Введите Ваш запрос: ","Текст запроса"),
           convers(Mygoal,Word_list),
           first_keyword_in_sentence(Word_list,First_keyword),!.

/* Механизм вывода */
/* Начальное правило механизма вывода */
     go(_,Mygoal):-
           not(rule(_,Mygoal,_,_)),!,
           concat("Рекомендуемая игра: ",Mygoal,Temp),
           concat(Temp,".",Result),
           dlg_Note("Экспертное заключение : ",Result).
     go(History,Mygoal):-
           rule(Rule_number,Mygoal,Type_of_breed,Conditions),
           check(Rule_number,History,Conditions),
           go([Rule_number|History],Type_of_breed).
/* Сопоставление входных данных пользователя со списками атрибутов
   отдельных игр */
     check(Rule_number,History,[Breed_cond|Rest_breed_cond_list]):-
           yes(Breed_cond),!,
           check(Rule_number,History,Rest_breed_cond_list).
     check(_,_,[Breed_cond|_]):-
           no(Breed_cond),!,fail.
     check(Rule_number,History,[Breed_cond|Rest_breed_cond_list]):-
           cond(Breed_cond,Text),
           ask_question(Breed_cond,Text),
           check(Rule_number,History,Rest_breed_cond_list).
     check(_,_,[]).
     do_answer(Cond_number,1):-!,
           assertz(yes(Cond_number)).
     do_answer(Cond_number,2):-!,
           assertz(no(Cond_number)),fail.      
/* Исключение данных из базы знаний 
   после завершения цикла "Распознавание-действие" */
     erase:-retract(_),fail.
     erase.
/* Уничтожение в базе данных всех ответов yes (да) и no (нет) */
     clear:-retract(yes(_)),retract(no(_)),fail,!.
     clear.
%BEGIN Task Window, e_Create
  task_win_eh(_Win,e_Create(_),0):-!,
%BEGIN Task Window, InitControls, 21:26:22-22.12.2007, Code automatically updated!
%END Task Window, InitControls
%BEGIN Task Window, ToolbarCreate, 21:26:22-22.12.2007, Code automatically updated!
	tb_project_toolbar_Create(_Win),
	tb_help_line_Create(_Win),
%END Task Window, ToolbarCreate
ifdef use_message
	msg_Create(100),
enddef
	!.
%END Task Window, e_Create

%MARK Task Window, new events

%BEGIN Task Window, id_file
  task_win_eh(_Win,e_Menu(id_file,_ShiftCtlAlt),0):-!,
        erase,
        assert_database,
	do_consulting,!.

%END Task Window, id_file

%BEGIN Task Window, id_help_contents
  task_win_eh(_Win,e_Menu(id_help_contents,_ShiftCtlAlt),0):-!,
  	vpi_ShowHelp("logic_es_win.hlp"),
	!.
%END Task Window, id_help_contents

%BEGIN Task Window, id_help_about
  task_win_eh(Win,e_Menu(id_help_about,_ShiftCtlAlt),0):-!,
	dlg_about_dialog_Create(Win),
	!.
%END Task Window, id_help_about

%BEGIN Task Window, id_file_exit
  task_win_eh(Win,e_Menu(id_file_exit,_ShiftCtlAlt),0):-!,
  	win_Destroy(Win),erase,
	!.
%END Task Window, id_file_exit

%BEGIN Task Window, e_Size
  task_win_eh(_Win,e_Size(_Width,_Height),0):-!,
ifdef use_tbar
	toolbar_Resize(_Win),
enddef
ifdef use_message
	msg_Resize(_Win),
enddef
	!.
%END Task Window, e_Size

%END_WIN Task Window

/***************************************************************************
		Invoking on-line Help
***************************************************************************/

  project_ShowHelpContext(HelpTopic):-
  	vpi_ShowHelpContext("logic_es_win.hlp",HelpTopic).

/***************************************************************************
			Main Goal
***************************************************************************/

goal

ifdef use_mdi
  vpi_SetAttrVal(attr_win_mdi,b_true),
enddef
ifdef ws_win
  ifdef use_3dctrl
    vpi_SetAttrVal(attr_win_3dcontrols,b_true),
  enddef
enddef  
  vpi_Init(task_win_Flags,task_win_eh,task_win_Menu,"logic_es_win",task_win_Title).

%BEGIN_TLB Project toolbar, 18:45:04-21.12.2007, Code automatically updated!
/**************************************************************************
	Creation of toolbar: Project toolbar
**************************************************************************/

clauses

  tb_project_toolbar_Create(_Parent):-
ifdef use_tbar
	toolbar_create(tb_top,0xC0C0C0,_Parent,
		[tb_ctrl(id_file_new,pushb,idb_new_up,idb_new_dn,idb_new_up,"New;New file",1,1),
		 tb_ctrl(id_file_open,pushb,idb_open_up,idb_open_dn,idb_open_up,"Open;Open file",1,1),
		 tb_ctrl(id_file_save,pushb,idb_save_up,idb_save_dn,idb_save_up,"Save;File save",1,1),
		 separator,
		 tb_ctrl(id_edit_undo,pushb,idb_undo_up,idb_undo_dn,idb_undo_up,"Undo;Undo",1,1),
		 tb_ctrl(id_edit_redo,pushb,idb_redo_up,idb_redo_dn,idb_redo_up,"Redo;Redo",1,1),
		 separator,
		 tb_ctrl(id_edit_cut,pushb,idb_cut_up,idb_cut_dn,idb_cut_up,"Cut;Cut to clipboard",1,1),
		 tb_ctrl(id_edit_copy,pushb,idb_copy_up,idb_copy_dn,idb_copy_up,"Copy;Copy to clipboard",1,1),
		 tb_ctrl(id_edit_paste,pushb,idb_paste_up,idb_paste_dn,idb_paste_up,"Paste;Paste from clipboard",1,1),
		 separator,
		 separator,
		 tb_ctrl(id_help_contents,pushb,idb_help_up,idb_help_down,idb_help_up,"Help;Help",1,1)]),
enddef
	true.
%END_TLB Project toolbar

%BEGIN_TLB Help line, 18:45:04-21.12.2007, Code automatically updated!
/**************************************************************************
	Creation of toolbar: Help line
**************************************************************************/

clauses

  tb_help_line_Create(_Parent):-
ifdef use_tbar
	toolbar_create(tb_bottom,0xC0C0C0,_Parent,
		[tb_text(idt_help_line,tb_context,452,0,4,10,0x0,"")]),
enddef
	true.
%END_TLB Help line

%BEGIN_DLG About dialog
/**************************************************************************
	Creation and event handling for dialog: About dialog
**************************************************************************/

constants

%BEGIN About dialog, CreateParms, 21:22:44-23.5.2021, Code automatically updated!
  dlg_about_dialog_ResID = idd_dlg_about
  dlg_about_dialog_DlgType = wd_Modal
  dlg_about_dialog_Help = idh_contents
%END About dialog, CreateParms

predicates

  dlg_about_dialog_eh : EHANDLER

clauses

  dlg_about_dialog_Create(Parent):-
	win_CreateResDialog(Parent,dlg_about_dialog_DlgType,dlg_about_dialog_ResID,dlg_about_dialog_eh,0).

%BEGIN About dialog, idc_ok _CtlInfo
  dlg_about_dialog_eh(_Win,e_Control(idc_ok,_CtrlType,_CtrlWin,_CtrlInfo),0):-!,
	win_Destroy(_Win),
	!.
%END About dialog, idc_ok _CtlInfo
%MARK About dialog, new events

  dlg_about_dialog_eh(_,_,_):-!,fail.

%END_DLG About dialog

