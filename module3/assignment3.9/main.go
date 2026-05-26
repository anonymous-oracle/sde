package main

import "fmt"

type LinkState int
const (
	StateOffline = iota
	StateOnline
	StateDegraded
)

type TelemetryIngester interface {
	InboundPayload(bytes int) error
	CheckConnectionState() LinkState
}

type SecureLink struct {
	NodeName string
	CurrentState LinkState
	TotalProcessed int
}

type OpenLink struct {
	BroadcastID int
	FixedStatus LinkState
}

func (openLink OpenLink) InboundPayload(bytes int) error {
	return nil
}

func (openLink OpenLink) CheckConnectionState() LinkState {
	return openLink.FixedStatus
}

func (secLink *SecureLink) InboundPayload(bytes int) error {
	if bytes < 0 {
		return fmt.Errorf("Well, nothing interesting over here...")
	}
	secLink.TotalProcessed += bytes
	return nil
}

func (secLink *SecureLink) CheckConnectionState() LinkState {
	return secLink.CurrentState
}

type AgnosticRouter struct {
	ActiveLinks map[string]TelemetryIngester
}

func (router *AgnosticRouter) ProcessChannel(channelKey string, dataSize int) {
	if _, ok := router.ActiveLinks[channelKey]; !ok {
		return
	} else {
		defer func (){
			if r := recover(); r!=nil {
				fmt.Println("Panic Intercepted:", r)
				return
			}
		}()
	}
	ingester, _ := router.ActiveLinks[channelKey]
	switch ingester := ingester.(type) {
	case *SecureLink:
		err := ingester.InboundPayload(dataSize)
		if err != nil {
			panic(err)
		} else if dataSize == 999 {
			panic("CRITICAL_ROUTER_JAM")
		}
		dataSize = 0
		fmt.Println(dataSize)
	case OpenLink:
		fmt.Println(dataSize)
		fmt.Println(ingester.BroadcastID)
	}
}
var _ TelemetryIngester = (*SecureLink)(nil)
var _ TelemetryIngester = nil 
func main() {
	router := AgnosticRouter{ ActiveLinks: make(map[string]TelemetryIngester)}
	router.ActiveLinks["channel-secure"] = &SecureLink{NodeName: "Secure-Alpha", CurrentState: StateOnline, TotalProcessed: 0}
	router.ActiveLinks["channel-open"] = OpenLink{BroadcastID: 707, FixedStatus: StateDegraded}
	router.ProcessChannel("channel-open", 512)
	router.ProcessChannel("channel-secure", 256)
	router.ProcessChannel("channel-secure", 999)
}